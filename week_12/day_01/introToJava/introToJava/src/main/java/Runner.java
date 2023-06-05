public class Runner {

    public static void main(String[] args) {
//        Cat myCat = new Cat();
//        myCat = new Dog();
//        System.out.println(myCat.meow());
        Bear bear = new Bear("Balu", 25, 95.62);
        String name = bear.getName();
        System.out.println(name);
        bear.setName("Baloo");
        System.out.println(bear.getName());
    }
}
