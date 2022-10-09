import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {

  constructor(private http: HttpClient, private route: Router) { }
  file: any;
  result: any;
  message: any;
  error: any;


  getFile(event: any) {
    this.file = event.target.files[0];
    console.log("file", this.file);
  }
  onSubmit() {
    let formData = new FormData();
    formData.append("file", this.file);
    this.http.post("http://localhost:5000/main", formData)
      .subscribe((result: any) => {
        this.result = result;
        this.error = result.error;
        if (this.error == 1) {
          this.message = result.message
          this.route.navigate(['/dashboard'])
          alert(this.message);
        } else {
          this.message = result.message;
          alert(this.message);
        }
      })
  }

}
