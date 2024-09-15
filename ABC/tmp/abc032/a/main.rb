a, b, n = 3.times.map{gets.to_i}

while(true) do
    if n % a == 0 && n % b == 0
        puts n
        exit
    end
    n += 1
end