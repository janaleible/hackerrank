<?php

class Person{
   public $age;
   public function __construct($initialAge) {

        if ($initialAge < 0) {
          echo "Age is not valid, setting age to 0.\n";
          $initialAge = 0;
        }

        $this->age = $initialAge;
    }

   public  function amIOld() {
       if($this->age < 13) {
           echo "You are young.\n";
       } elseif($this->age < 18) {
           echo "You are a teenager.\n";
       } else {
           echo "You are old.\n";
       }
    }

   public  function yearPasses() {
        $this->age++;
   }
}

// evaluation code -- already given

$T = intval(fgets(STDIN));
 for($i=0;$i<$T;$i++){
     $age=intval(fgets(STDIN));
     $p=new Person($age);
     $p->amIOld();
     for($j=0;$j<3;$j++){
         $p->yearPasses();
     }
     $p->amIOld();
     echo "\n";

 }
?>