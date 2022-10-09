import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SigninService {


  constructor(private httpClient: HttpClient) { }

  signin(data:any){
    return this.httpClient.post("http://localhost:5000/signin", data)
  }
}
