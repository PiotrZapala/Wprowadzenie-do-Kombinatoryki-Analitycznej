using TaylorSeries
using Plots

shift_taylor(a) = a + Taylor1(typeof(a), 100)

t = shift_taylor(0.0)
x = 1 / (1 - t)^t

print(x.coeffs)

plt = plot(x.coeffs, color=:red, label="x.coeffs", xlabel="n", ylabel="Coefficient")

f(x) = 1 / (1 + exp(-x))

x_values = range(0, stop=100, length=100)

plot!(plt, x_values, f.(x_values), color=:blue, label="1 / (1 + exp(-x))")

display(plt)