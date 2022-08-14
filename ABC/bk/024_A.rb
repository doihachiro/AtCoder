A, B, C, K = gets.split.map(&:to_i)
S, T = gets.split.map(&:to_i)

if S + T >= K
    puts (A - C) * S + (B - C) * T
else
    puts A * S + B * T
end