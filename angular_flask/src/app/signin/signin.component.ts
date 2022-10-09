import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent{

  data: any;
  error: any;
  message: any;
  result: any;
  message1 : any;

  constructor(private http : HttpClient, 
    private route: Router
    ){}

  onSubmit(data:{email:string,password:string}){
   console.log(data);
   this.http.post("http://localhost:5000/signin", data)
   .subscribe((result: any)=>{
     this.result = result;
     this.error = result.error;
     if (this.error == 1){
      this.message1 = result.message 
      this.route.navigate(['/main'])
      alert(this.message1);
     }else{
      this.message = result.message;
      alert(this.message);
     }
     
   })
  }
  
 
}
