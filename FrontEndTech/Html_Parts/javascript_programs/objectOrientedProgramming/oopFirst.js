class person{

    constructor(age,name){
        this.age=age;
        this.name=name;
    }
    printPerson=()=>{
        console.log(this.name);
        console.log(this.age)

    }
}
// instance variable initi
//__init__()

var obj1=new Person(25,"ajay")
obj1.printPerson()