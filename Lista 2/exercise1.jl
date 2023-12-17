using Plots

function sd(n)
    return sum(digits(n, base=2))
end

function s(n)
    result = 0
    for k in 1:n
        result += sd(k)
    end
    return result
end

function asymptote(n)
    return c * n * log2(n)
end

function plot_s(n_max)
    n_values = 1:n_max
    s_values = [s(n) for n in n_values]
    a_values = [asymptote(n) for n in n_values]

    plot(n_values, s_values, label="s(n)", xlabel="n", ylabel="s(n)", linewidth=2)
    plot!(n_values, a_values, label="a(n)", linestyle=:dash, linewidth=2)
    display(plot!())

    diff_values = s_values .- a_values
    plot(n_values, diff_values, label="s(n) - a(n)", xlabel="n", ylabel="s(n) - a(n)", linewidth=2)
    display(plot!())
end

c = 0.5

plot_s(1024)
