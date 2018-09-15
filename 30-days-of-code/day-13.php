<?php
abstract class Book
{
    
    protected $title;
    protected  $author;
    
     function __construct($t,$a){
        $this->title=$t;
        $this->author=$a;
    }
    abstract protected function display();
}

class MyBook extends Book {
    function __construct(string $title,  string $author, int $price) {
        $this->price = $price;
        parent::__construct($title, $author);
    }
    
    function display() {
        print("Title: " . $this->title);
        print("Author: " . $this->author);
        print("Price: " . $this->price);
    }
}

$title=fgets(STDIN);
$author=fgets(STDIN);
$price=intval(fgets(STDIN));
$novel=new MyBook($title,$author,$price);
$novel->display();