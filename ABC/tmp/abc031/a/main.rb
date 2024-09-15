A, D = gets.split.map(&:to_i)

X = (A + 1) * D
Y = A * (D + 1)

puts X > Y ? X : Y