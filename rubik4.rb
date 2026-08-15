# rubik4.rb — Ruby версия

class Rubik4
  attr_reader :faces, :moves

  def initialize
    @faces = Array.new(6) { Array.new(4) { Array.new(4) } }
    colors = [0,1,2,3,4,5]
    6.times do |f|
      4.times do |i|
        4.times do |j|
          @faces[f][i][j] = colors[f]
        end
      end
    end
    @moves = []
  end

  def print_cube
    puts "Развёртка (U D L R F B):"
    6.times do |f|
      puts "Грань #{f}:"
      @faces[f].each do |row|
        puts row.join(' ')
      end
    end
  end

  def do_move(move)
    @moves << move
    puts "Ход: #{move}"
  end

  def scramble
    moves_list = %w[R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3]
    20.times do
      m = moves_list.sample
      do_move(m)
    end
  end
end

def main
  rubik = Rubik4.new
  puts "🧩 Rubik's Cube 4×4 Simulator (Ruby)"
  puts "Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit"

  loop do
    print "> "
    cmd = gets.chomp.strip.downcase
    case cmd
    when "quit" then break
    when "show" then rubik.print_cube
    when "scramble" then rubik.scramble
    when "reset" then rubik = Rubik4.new
    when "help" then puts "Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit"
    else rubik.do_move(cmd)
    end
  end
end

main if __FILE__ == $0
