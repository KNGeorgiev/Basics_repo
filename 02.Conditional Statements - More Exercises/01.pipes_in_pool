pool_volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours = float(input())

first_pipe_volume = first_pipe * hours
second_pipe_volume = second_pipe * hours
total_volume = first_pipe_volume + second_pipe_volume
total_volume_percentage = total_volume / pool_volume * 100
first_pipe_percentage = first_pipe_volume / total_volume * 100
second_pipe_percentage = second_pipe_volume / total_volume * 100


if total_volume > pool_volume:
    print(f"For {hours} hours the pool overflows with {total_volume - pool_volume:.2f} liters.")

else:
    print(f"The pool is {total_volume_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. \
    Pipe 2: {second_pipe_percentage:.2f}%.")
    
