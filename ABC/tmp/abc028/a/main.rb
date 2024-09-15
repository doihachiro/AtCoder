N = gets.to_i

if N < 60
    puts "Bad"
elsif N < 90
    puts "Good"
elsif N < 100
    puts "Great"
elsif N == 100
    puts "Perfect"
end