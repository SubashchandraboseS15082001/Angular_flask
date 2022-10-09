import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent{

  constructor(private http: HttpClient) { }

result:any;
error:  any;
message: any;
value = "";
predicted_val: any;
value_dis: any;


  onSubmit(data:{television:string, radio:string, newspaper:string}){
    console.log(data);
    this.http.post("http://localhost:5000/dashboard", data)
    .subscribe((result: any)=>{

      this.result = result;
       this.error = result.error;
       if (this.error == 1){
        this.message = result.message
        // this.route.navigate(['/signin'])
        alert("Model predicted the sale!");
        this.value_dis = "Predicted Sales for given data is "
        this.predicted_val = result.predicted_val
        this.value = "Click  here to redirect to the dashboard!"
        
       }else{
        this.message = result.message;
        alert(this.message);
       }
    })

}
}
