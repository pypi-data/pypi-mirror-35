#include <math.h>
#include <mkl.h>

typedef radial_set {
	int X; ///< number of radial functions;
	double** Ps; ///< XxN
	double** Pinvrs; ///< XxN
} radial_set_t;

typedef struct radial_set {
	int l; ///< angular momentum quantum number
	int v; ///< valence level
	int X; ///< number of basis functions/wavefunction solutions per l
	int* occs; ///< (X) number of electrons in a shell
	double* h; ///< single particle hamiltonian (XxX)
	double*** ee; ///< electron-electron repulsion terms 4x(XxX)x(XxX) 0 2 4 6
	double* es; ///< (X)
	double** Ps; ///< (L)x(XxX)
	double* r; ///< (N)
	double*** yks; ///< (XxX)x(4)x(N) 0 2 4 6
	double* DM; ///< density matrix (XxX)
	double E; ///< total energy
} radial_set_t;

typedef struct awf {
	int Z; ///< atomic number/number of electrons
	int L; ///< number of l quantums numbers, ie lmax+1
	int X; ///< number of basis functions/wavefunction solutions per l
	int N; ///< grid size
	radial_set_t* wfs; ///< L radial_set_t wavefunctions
	double E; ///< total energy
} awf_t;

double* discrete_sp_hamiltonian(int Z, int l, int size, double* r) {
	double* h = (double*) calloc(size * size * sizeof(double));

	for (int i = 0; i < N - 1; i++) {
		dR = r[i+1] - r[i];
		h[N*i+i] = 1/(r[i+1]-r[i]) + 1/(r[i]-r[i-1])
					- 2*Z/r[i] + l*(l+1)/r[i]/r[i]
					- 2/r[i]*yks[i*X+i];
		h[N*i+i+1] = -1/(r[i+1]-r[i]);
		h[N*(i+1)+i] = h[N*i+i+1];
		h[N*i+i-1] = -1/(r[i]-r[i-1]);
		h[N*(i-1)+i] = h[N*i+i-1];
	}
}

awf_t* construct_basis(int Z, int N, int maxN, int maxL, double* r) {
	int X = maxN;
	int L = maxL + 1;
	radial_set_t* wfs = (radial_set_t*) malloc(L * sizeof(radial_set_t));

	for (int l = 0; l < L; l++) {
		double* h = (double*) calloc(X * X, sizeof(double));
		int* ls = (int*) malloc(X * sizeof(int));
		int* occs = (int*) calloc(X, sizeof(int));
		double** bfs = (double**) malloc(X * sizeof(double*));
		double*** splines = (double***) malloc(X * sizeof(double**));
		for (int n = 1; n <= maxN; n++) {
			double* bf = (double*) malloc(N * sizeof(double*));
			for (int j = 0; j < N; j++) {
				bf[j] = r[j] * hradial(n, l, r[j]);
			}
			bfs[n-1] = bf;
			splines[n-1] = spline_coeff(r, bf, N);
			h[X*n-X+n-1] = -0.5*Z*Z/(n+l)/(n+l);
		}
		double*** yks = (double***) malloc(X*X * sizeof(double**));
		int b1, b2;
		for (int i = 0; i < X * X; i++) {
			b1 = i / X;
			b2 = i % X;
			yks[i] = (double**) malloc(4 * sizeof(double*));
			for (int knum = 0; knum < 4; knum++) {
				yks[i][knum] = yk(knum*2, N, r, bfs[b1], bfs[b2]);
			}
		}
		double*** ees = (double***) malloc(4 * sizeof(double**));
		for (int knum = 0; knum < 4; knum++) {
			ees[knum] = (double**) malloc(X*X * sizeof(double*));
			int b3, b4;
			for (int i = 0; i < X * X; i++) {
				ees[knum][i] = (double*) malloc(X*X * sizeof(double));
				b1 = i / X;
				b2 = i % X;
				for (int j = 0; j < X * X; j++) {
					b3 = j / X;
					b4 = j % X;
					double* integrand = (double*) malloc(N * sizeof(double));
					for (int rnum = 0; rnum < N; rnum++) {
						integrand[rnum] = yks[j][knum][rnum] * bfs[b1] * bfs[b2] / r[rnum];
					}
					double** spline = spline_coeff(r, integrand, N);
					ees[knum][i][j] = spline_integral(r, integrand, spline, N);
					free(spline[0]);
					free(spline[1]);
					free(spline[2]);
					free(spline);
					free(integrand);
				}
			}
		}

		wfs[l].l = l;
		wfs[l].v = 0;
		wfs[l].X = X;
		wfs[l].ee = ees;
		wfs[l].h = h;
		wfs[l].occs = occs;
		wfs[l].yks = yks;
		wfs[l].r = r;
	}

	awf_t* wf = (awf_t*) malloc(sizeof(awf_t));
	wf->wfs = wfs;
	wf->L = L;
	wf->X = X;
	wf->N = N;
	wf->Z = 1;
	double E = 0;

	return wf;
}

awf_t* setup_H(int N, int maxN, int maxL, double* r) {
	awf_t* wf = construct_basis(1, N, maxN, maxL, r);
	for (int l = 0; l < wf->L; l++) {
		radial_set_t* rwf = wf->wfs[l];
		int X = rwf->X;
		for (int b = 0; b < X; b1++) {
			rwf->Ps[b*X+b] = 1.0;
		}
	}
	wf->wfs[0].occs[0] = 1;
	wf->Z = 1;
	return wf;
}

void assign_occs(awf_t* wf) {
	for (int l = 0; l < wf->L; l++) {
		for (int b = 0; b < wf->wfs[l].X; b++) {
			wf->wfs[l].occs[b] = 0;
		}
		wf->wfs[l].v = 0;
	}
	int reme = wf->Z;
	int nume = 0;
	int minl = 0;
	double teste = 0;
	double mine = 10000;
	while (reme > 0) {
		for (int l = 0; l < wf->L; l++) {
			teste = wf->wfs[l].es[wf->wfs[l].v];
			if (teste < mine) {
				mine = teste;
				minl = l;
			}
		}
		if (reme > 4*minl+2) {
			reme -= 4*minl+2;
			wf->wfs[minl].occs[wf->wfs[minl].v] = 4*minl+2;
			wf->wfs[minl].v++;
		} else {
			wf->wfs[minl].occs[wf->wfs[minl].v] = reme;
			wf->wfs[minl].v++;
			reme = 0;
		}
	}
}

awf_t* setup(int Z, int N, int maxN, int maxL, double* r, double** P0s) {
	awf_t* wf = construct_basis(Z, N, maxN, maxL, r);
	for (int l = 0; l < wf->L; l++) {
		wf->wfs[l].Ps = P0s[l];
	}
	wf->Z = Z;
	assign_occs(awf_t* wf);
	return wf;
}

void make_density_matrix(radial_set_t* wf) {
	int X = wf->X;
	wf->DM = (double*) malloc(X*X * sizeof(double));
	for (int i = 0; i < X; i++) {
		wf->DM[i*X+i] = wf->occs[i];
	}
	double* temp = (double*) malloc(X*X * sizeof(double));

	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasTrans, X, X, X, 1, wf->DM, X, wf->Ps, X, 0, temp, X);
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, X, X, X, 1, wf->Ps, X, temp, X, 0, wf->DM, X);
	free(temp);
}

LAPACKE_dsyevd(LAPACKE_ROW_MAJOR, 'V', 'U', X, hamiltonian, X, es);

void solve(awf_t* wf, int maxsteps) {

	int X = wf->X;
	for (int step = 0; step < maxsteps; step++) {
		for (int l = 0; l < wf->L; l++) {

			radial_set_t* rwf = wf->wfs[l];

			double* hamiltonian = (double*) malloc(X * X * sizeof(double));

			make_density_matrix(rwf->Ps);
			double J, K;
			for (int mu = 0; mu < X; mu++) {
				for (int nu = 0; nu < X; nu++) {
					hamiltonian[X*mu+nu] = rwf->h[X*mu+nu];
					for (int lj = 0; lj < wf->L; lj++) {
						double* DM = wf->wfs[lj].DM;
						double** ee = wf->wfs[lj].ee[lj];
						for (int lambda = 0; lambda < X; lambda++) {
							for (int sigma = 0; sigma < X; sigma++) {
								J = ee[mu*X+nu][lambda*X+sigma];
								hamiltonian[X*mu+nu] += DM[lambda*X+sigma] *
									();
							}
						}
					}
					double* DM = wf->wfs[l].DM;
					double** ee = wf->wfs[l].ee[l];
					for (int lambda = 0; lambda < X; lambda++) {
						for (int sigma = 0; sigma < X; sigma++) {
							J = ee[mu*X+nu][lambda*X+sigma];
							hamiltonian[X*mu+nu] += DM[lambda*X+sigma] *
								();
						}
					}
				}
			}
		}
	}
}

double* yk(int k, int size, double* r, double* P1, double* P2) {
	int size1 = rnum+1;
	int size2 = size-rnum;

	double* integrand1 = (double*) malloc(size * sizeof(double));
	double* integrand2 = (double*) malloc(size * sizeof(double));

	for (int i = 0; i < size; i++) {
		integrand1[i] = P1[i] * P2[i] * pow(r[i], k-1); //might need to change to k
	}
	double** spline1 = spline_coeff(grid, integrand1, size);
	for (int i = 0; i < size; i++) {
		integrand2[i] = P1[i] * P2[i] * pow(r[i], -k-2); //might need to change to -k-1
	}
	double** spline2 = spline_coeff(grid, integrand2, size);
	integrals1[0] = r[0] * P1[0];
	integrals2[size-1] = 0;
	double* a = integrand1, b = spline1[0], c = spline1[1], d = spline1[2];
	double* a = integrand2, b = spline2[0], c = spline2[1], d = spline2[2];
	double dx=0;
	for (int i = 0; i < size-1; i++) {
		dx = r[i+1] - r[i];
		integrals1[i+1] = integral1s[i] + dx * (a[i] + dx * (b[i]/2 + dx * (c[i]/3 + d[i]*dx/4)));
		integrals1[i+1] *= pow(r[i], -k);
		j = size - i - 2;
		dx = r[j] - r[j-1];
		integrals2[j] = integrals2[j+1] + dx * (e[j] + dx * (f[j]/2 + dx * (g[i]/3 + h[j]*dx/4)));
		integrals2[j] *= power(r[j], k+1);
	}

	for (int i = 0; i < size; i++) {
		intgrals1[i] += integrals2[i];
	}

	free(integrals2);
	free(integrand1);
	free(integrand2);
	free(spline1[0]);
	free(spline1[1]);
	free(spline1[2]);
	free(spline2[0]);
	free(spline2[1]);
	free(spline2[2]);
	return integrals1;

}

double* sp_hamiltonian() {

}

void construct_hamiltonian(awf_t* wf, double* H) {
	int N = wf->N;
	int X = wf->X;
	double* r = wf->r;
	for (int i = 0; i < X; i++) {
		for (j = 0; j < N; j++) {
			H
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < X; j++) {
			H[N*i+i] += 2*wf->occs[j]/r[j] * yks[X*j+j][0][i];
		}
		H[N*i+i] = 1/(r[i+1]-r[i]) + 1/(r[i]-r[i-1])
					- 2*Z/r[i] + l*(l+1)/r[i]/r[i]
					- 2/r[i]*yks[i*X+i];
		H[N*i+i+1] = -1/(r[i+1]-r[i]);
		H[N*(i+1)+i] = H[N*i+i+1];
		H[N*i+i-1] = -1/(r[i]-r[i-1]);
		H[N*(i-1)+i] = H[N*i+i-1];
	}

	for (int i = 0; i < N; i++) {
		H[N*i+i] = 1/(r[i+1]-r[i]) + 1/(r[i]-r[i-1])
					- 2*Z/r[i] + l*(l+1)/r[i]/r[i]
					- 2/r[i]*ykbfs[i*X+i];
		H[N*i+i+1] = -1/(r[i+1]-r[i]);
		H[N*(i+1)+i] = H[N*i+i+1];
		H[N*i+i-1] = -1/(r[i]-r[i-1]);
		H[N*(i-1)+i] = H[N*i+i-1];
	}
}

integral += dx * (a[i] + dx * (b[i]/2 + dx * (c[i]/3 + d[i]*dx/4)));