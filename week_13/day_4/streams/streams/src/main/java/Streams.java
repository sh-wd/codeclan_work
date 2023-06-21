import java.util.Arrays;
import java.util.List;
import java.util.OptionalDouble;
import java.util.stream.Stream;

public class Streams {

    public static void main(String[] args) {
        List<String> myList = Arrays.asList("Amanda", "Alex", "Sandy", "Alina", "Skye");
//        List - an interface that ArrayLists implements
//        Arrays - a class with methods for manipulating arrays
//        .asList - extracts the array items as a list

//        myList
//                .stream()

//        Stream.of("Amanda", "Alex", "Sandy", "Alina", "Skye")
////                .map(String::toUpperCase)
//                .map(name -> name.toUpperCase())
//                .forEach(System.out::println);

        int total = Stream.of(1, 2, 3, 4, 5)
                .reduce(0, (sum, num) -> sum += num);
//        System.out.println(total);

//        Stream.of(99, 3, 61, 20, 83, 12, 2, 18, 10)
//                .sorted()
//                .limit(4)
//                .forEach(System.out::println);

        OptionalDouble average = Stream.of(99, 3, 61, 20, 83, 12, 2, 18, 10)
                .mapToInt(number -> number)
                .average();
//        System.out.println(average);

        int result = Stream.of(99, 3, 61, 20, 83, 12, 2, 18, 10)
                .mapToInt(n -> n)
                .max()
                .getAsInt();
//        System.out.println(result);


        int output = Stream.of(99, 3, 61, 20, 83, 12, 2, 18, 10)
                .peek(n -> System.out.println("original " + n))
                .map(n -> n * 2)
                .peek(n -> System.out.println("double " + n))
                .filter(n -> n % 3 == 0)
                .peek(n -> System.out.println("filtered " + n))
                .reduce(0, (sum, num) -> sum += num);
        System.out.println(output);
    }
}
