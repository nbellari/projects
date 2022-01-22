list = [0, 1, 2, 3, 4, 5, 6]

begin
    puts list[1]
    num = 10 / 0
rescue TypeError => exception
    puts exception
rescue ZeroDivisionError => exception
    puts exception
end
