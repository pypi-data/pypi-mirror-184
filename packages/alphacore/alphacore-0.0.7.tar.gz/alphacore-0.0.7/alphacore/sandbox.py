from fit_distribution import Fit_Weibull_2P, Fit_Normal_2P

failures = [4, 8, 12, 15, 25, 28]
right_censored = [7, 8, 9, 12, 29, 40]
method = "MLE"
res = Fit_Weibull_2P(failures=failures, right_censored=right_censored, method=method)
res2 = Fit_Normal_2P(failures=failures, right_censored=right_censored, method=method)

from reliability.Fitters import Fit_Weibull_2P, Fit_Normal_2P

resrel = Fit_Weibull_2P(
    failures=failures, right_censored=right_censored, print_results=False, method=method
)
resrel2 = Fit_Normal_2P(
    failures=failures, right_censored=right_censored, print_results=False, method=method
)

print(res.alpha-resrel.alpha)
print(res.beta-resrel.beta)
print(res2.mu-resrel2.mu)
print(res2.sigma-resrel2.sigma)

