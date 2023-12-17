function sigma(n)
    divisors = Int64[]
    for i in 1:n
        if n % i == 0
            push!(divisors, i)
        end
    end
    
    return sum(divisors)
end

function calculate_pn(n_max)
    p = ones(Float64, n_max)
    for n in 2:n_max
        for j in 1:(n-1)
            p[n] = p[n] + (sigma(j) * p[n - j])
            println(p[n])
        end
        p[n] = p[n]/n
    end
    return p
end

n_max = 100
p_values = calculate_pn(n_max)
println("p_n values for n = 1 to $n_max:")
for (n, value) in enumerate(p_values)
    println("p_$n = $value")
end
