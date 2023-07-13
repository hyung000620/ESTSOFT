let animal = "cat";
switch(animal){
    case "dog":
        console.log("Bark");
        break;
    case "cat":
        console.log("Meow");
        break;
    case "bird":
        console.log("Tweet");
        break;
    default:
        console.log("Unknown animal");
}

if (animal == "dog"){
    console.log("Bark");
}
else if (animal == "cat"){
    console.log("Meow");
}
else if (animal == "bird"){
    console.log("Tweet");
}  
else{
    console.log("Unknown animal");
}
    