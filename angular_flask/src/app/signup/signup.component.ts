import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {
  result: any;
  error: any;
  message: any;
  message1: any;
  

  constructor(private http : HttpClient, private route: Router){}

 onSubmit(data:{username:string,email:string,password:string}){
  console.log(data);
  this.http.post("http://localhost:5000/signup", data)
  .subscribe((result: any)=>{
    this.result = result;
     this.error = result.error;
     if (this.error == 1){
      this.message1 = result.message
      this.route.navigate(['/signin'])
      alert(this.message1);
     }else{
      this.message = result.message;
      alert(this.message);
     }
  })
 }

}
