N = gets.chomp.split("").uniq
puts N.size == 1 ? "SAME" : "DIFFERENT"