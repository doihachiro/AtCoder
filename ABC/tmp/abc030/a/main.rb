A, B, C, D = gets.split.map(&:to_i)

X = B.quo(A).to_f
Y = D.quo(C).to_f

if X > Y
    puts "TAKAHASHI"
elsif X < Y
    puts "AOKI"
elsif X == Y
    puts "DRAW"
end