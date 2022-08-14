N = gets.split.map(&:to_i)
puts N.find{|n| N.count(n) % 2 == 1}