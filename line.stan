data {
    int<lower=1> N;
    vector[N] x;
    vector[N] y;
    vector<lower=0>[N] x_err;
    vector<lower=0>[N] y_err;
}

parameters {
    real m;
    real c;
    vector[N] x_t; // true x values
    real<lower=0> x_err_int;
    real<lower=0> y_err_int;
}

model {
    x_err ~ normal(0, x_err_int);
    y_err ~ normal(0, y_err_int);
    x ~ normal(x_t, x_err);
    y ~ normal(c + m*x_t, y_err);
}