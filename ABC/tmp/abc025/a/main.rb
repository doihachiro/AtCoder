S = gets.chomp
N = gets.to_i

A, B = (N - 1).divmod(5)
puts S[A] + S[B]