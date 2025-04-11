class Student:
    # definido o nosso método construtor e atributos
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    # adicionando as notas
    def add_grade(self, grade):
        self.grades.append(grade)
    
    # mostrando a média entre as notas
    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    # Mostra se o aluno esta com mais de 60 na nota de 100
    @property
    def is_passing(self):
        return self.get_average_grade() >= 60
    
    # método que chama todos os outros métodos
    @classmethod
    def main(cls):
        # lista que recebe os estudantes
        students = []
        
        while True:
            # o nosso menu
            print("1 - Adicionar Aluno")
            print("2 - Adicionar Nota")
            print("3 - Verificar aprovação")
            print("4 - Apresentação do Aluno")
            print("5 - Sair")
            # Defiunição do índice do menu
            choice = int(input("Escolha uma opção: "))
            
            # Cadastro de alunos
            if choice == 1:
                name = input("Nome do Aluno: ")
                age = int(input("Idade do Aluno: "))
                student = cls(name, age)
                students.append(student)
                print("Aluno adicionado")
            
            # Cadastro de notas de alunos
            elif choice == 2:
                # verificação se existe objeto definido na lista de students
                if not students:
                    print("Nenhum aluno cadastrado!")
                    # se a lista for vazia volta para o menu
                    continue
                # forma o índice de aluno na lista de students
                for idx, student in enumerate(students):
                    print(f"{idx+1} - {student.name}")
                # opção de escolha o índice do aluno
                student_idx = int(input("Escolha o número do aluno: ")) -1
                
                if 0 <= student_idx < len(students): # verificar se o índicve esta cerrto
                    # Define a nota do aluno
                    grade = float(input("Nota do aluno: "))
                    # escolhendo o objeto na lista e inserindo a nota
                    students[student_idx].add_grade(grade)
                    print("Nota adicionada!")
                else:
                    print("Índice de aluno inválido!")
            
            elif choice == 3:
                if not students:
                    print("Nenhum aluno cadastrado!")
                    continue
                for student in students:
                    average_grade = student.get_average_grade()
                    if average_grade >= 6.0:
                        status = "Aprovado"
                    else:
                        status = "Reprovado"
                    
                    print(f"""
                          - Nome do estudante {student.name} 
                          - Média {average_grade} 
                          - Status {status}
                          """)
            
            elif choice == 4:
                # verificação se existe objeto definido na lista de students
                if not students:
                    print("Nenhum aluno cadastrado!")
                    # se a lista for vazia volta para o menu
                    continue
                # forma o índice de aluno na lista de students
                for idx, student in enumerate(students):
                    print(f"""
                        Matricula do aluno: {idx+1}
                        Nome do aluno  - {student.name}
                        Idade do aluno - {student.age}
                        Notas do aluno - {student.grades}
                          """)
            
            
            elif choice == 5:
                print("Saíndo....")
                print("Obrigado por usar o nosso sistema!")
                print("Até a próxima!")
                break
            
            else:
                print("Opção errada, escolha novamente!")

estudante = Student.main()

Java aluno

import java.util.ArrayList;
import java.util.Scanner;

public class Student {
    private String name;
    private int age;
    private ArrayList<Double> grades;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.grades = new ArrayList<>();
    }

    public void addGrade(double grade) {
        grades.add(grade);
    }

    public double getAverageGrade() {
        if (grades.isEmpty()) return 0;
        double sum = 0;
        for (double g : grades) {
            sum += g;
        }
        return sum / grades.size();
    }

    public boolean isPassing() {
        return getAverageGrade() >= 60;
    }

    public void printInfo(int index) {
        System.out.println("\nMatrícula do aluno: " + (index + 1));
        System.out.println("Nome do aluno: " + name);
        System.out.println("Idade do aluno: " + age);
        System.out.println("Notas do aluno: " + grades);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Student> students = new ArrayList<>();

        while (true) {
            System.out.println("\n1 - Adicionar Aluno");
            System.out.println("2 - Adicionar Nota");
            System.out.println("3 - Verificar Aprovação");
            System.out.println("4 - Apresentação do Aluno");
            System.out.println("5 - Sair");
            System.out.print("Escolha uma opção: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // limpar o buffer

            switch (choice) {
                case 1 -> {
                    System.out.print("Nome do Aluno: ");
                    String name = scanner.nextLine();
                    System.out.print("Idade do Aluno: ");
                    int age = scanner.nextInt();
                    students.add(new Student(name, age));
                    System.out.println("Aluno adicionado!");
                }
                case 2 -> {
                    if (students.isEmpty()) {
                        System.out.println("Nenhum aluno cadastrado!");
                        continue;
                    }
                    for (int i = 0; i < students.size(); i++) {
                        System.out.println((i + 1) + " - " + students.get(i).name);
                    }
                    System.out.print("Escolha o número do aluno: ");
                    int index = scanner.nextInt() - 1;
                    if (index >= 0 && index < students.size()) {
                        System.out.print("Nota do aluno: ");
                        double grade = scanner.nextDouble();
                        students.get(index).addGrade(grade);
                        System.out.println("Nota adicionada!");
                    } else {
                        System.out.println("Índice inválido!");
                    }
                }
                case 3 -> {
                    if (students.isEmpty()) {
                        System.out.println("Nenhum aluno cadastrado!");
                        continue;
                    }
                    for (Student s : students) {
                        String status = s.isPassing() ? "Aprovado" : "Reprovado";
                        System.out.printf("- Nome: %s | Média: %.2f | Status: %s%n",
                                s.name, s.getAverageGrade(), status);
                    }
                }
                case 4 -> {
                    if (students.isEmpty()) {
                        System.out.println("Nenhum aluno cadastrado!");
                        continue;
                    }
                    for (int i = 0; i < students.size(); i++) {
                        students.get(i).printInfo(i);
                    }
                }
                case 5 -> {
                    System.out.println("Saindo... Obrigado por usar o nosso sistema!");
                    return;
                }
                default -> System.out.println("Opção inválida! Tente novamente.");
            }
        }
    }
}


Animal PY

class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo.lower()

    def apresentar(self):
        print(f"Este é um {self.nome}, um animal do tipo {self.tipo}.")

    def movimentar(self, pode_correr, pode_nadar, pode_pular):
        if self.tipo == "voador":
            print(f"{self.nome} pode voar e andar.")
        elif self.tipo == "marinho":
            print(f"{self.nome} vive na água e pode nadar.", end=" ")
            if pode_pular:
                print("Também pode pular em terra.")
            else:
                print()
        elif self.tipo == "terrestre":
            print(f"{self.nome} vive na terra.", end=" ")
            if pode_correr:
                print("Pode correr.", end=" ")
            if pode_nadar:
                print("Pode nadar.", end=" ")
            if not pode_correr and not pode_nadar:
                print("Se movimenta andando ou rastejando.", end=" ")
            print()
        else:
            print("Tipo de animal desconhecido.")

# Função para ler sim/não e transformar em booleano
def ler_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'nao', 'não']:
            return False
        else:
            print("Resposta inválida. Digite 's' ou 'n'.")

# Lista para guardar os animais
animais = []

while True:
    nome = input("Digite o nome do animal: ")

    while True:
        tipo = input("O animal é 'terrestre', 'marinho' ou 'voador'? ").lower()
        if tipo in ['terrestre', 'marinho', 'voador']:
            break
        else:
            print("Tipo inválido. Tente novamente.")

    # Perguntar as habilidades
    pode_correr = ler_sim_nao("Ele pode correr?")
    pode_nadar = ler_sim_nao("Ele pode nadar?")
    pode_pular = ler_sim_nao("Ele pode pular?")

    # Criar e armazenar o animal
    animal = Animal(nome, tipo)
    animais.append((animal, pode_correr, pode_nadar, pode_pular))

    continuar = input("Deseja adicionar outro animal? (s/n): ").lower()
    if continuar not in ['s', 'sim']:
        break

# Mostrar todos os animais e como se movimentam
print("\n--- Lista de Animais ---")
for animal, correr, nadar, pular in animais:
    animal.apresentar()
    animal.movimentar(correr, nadar, pular)


main java animal

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        ArrayList<Animal> animais = new ArrayList<>();
        ArrayList<boolean[]> habilidades = new ArrayList<>();

        while (true) {
            System.out.print("Digite o nome do animal: ");
            String nome = entrada.nextLine();

            String tipo;
            while (true) {
                System.out.print("O animal é 'terrestre', 'marinho' ou 'voador'? ");
                tipo = entrada.nextLine().toLowerCase();
                if (tipo.equals("terrestre") || tipo.equals("marinho") || tipo.equals("voador")) {
                    break;
                } else {
                    System.out.println("Tipo inválido. Tente novamente.");
                }
            }

            boolean podeCorrer = lerSimNao(entrada, "Ele pode correr? (s/n): ");
            boolean podeNadar  = lerSimNao(entrada, "Ele pode nadar? (s/n): ");
            boolean podePular  = lerSimNao(entrada, "Ele pode pular? (s/n): ");

            Animal animal = new Animal(nome, tipo);
            animais.add(animal);
            habilidades.add(new boolean[] { podeCorrer, podeNadar, podePular });

            boolean continuar = lerSimNao(entrada, "Deseja adicionar outro animal? (s/n): ");
            if (!continuar) break;
        }

        System.out.println("\n--- Lista de animais ---");
        for (int i = 0; i < animais.size(); i++) {
            Animal animal = animais.get(i);
            boolean[] h = habilidades.get(i);
            animal.apresentar();
            animal.movimentar(h[0], h[1], h[2]);
            System.out.println();
        }

        entrada.close();
    }

    private static boolean lerSimNao(Scanner sc, String pergunta) {
        while (true) {
            System.out.print(pergunta);
            String resposta = sc.nextLine().trim().toLowerCase();
            if (resposta.equals("s") || resposta.equals("sim")) return true;
            else if (resposta.equals("n") || resposta.equals("nao") || resposta.equals("não")) return false;
            else System.out.println("Resposta inválida. Digite 's' ou 'n'.");
        }
    }
}


animal java

public class Animal {
    private String nome;
    private String tipo;

    public Animal(String nome, String tipo) {
        this.nome = nome;
        this.tipo = tipo.toLowerCase();
    }

    public void apresentar() {
        System.out.println("Este é um " + nome + ", um animal do tipo " + tipo + ".");
    }

    public void movimentar(boolean podeCorrer, boolean podeNadar, boolean podePular) {
        switch (tipo) {
            case "voador":
                System.out.println(nome + " pode voar e andar.");
                break;
            case "marinho":
                System.out.print(nome + " vive na água e pode nadar. ");
                if (podePular) System.out.print("Também pode pular em terra.");
                System.out.println();
                break;
            case "terrestre":
                System.out.print(nome + " vive na terra. ");
                if (podeCorrer) System.out.print("Pode correr. ");
                if (podeNadar) System.out.print("Pode nadar. ");
                if (!podeCorrer && !podeNadar) System.out.print("Se movimenta andando ou rastejando.");
                System.out.println();
                break;
            default:
                System.out.println("Tipo de animal desconhecido.");
        }
    }
}
