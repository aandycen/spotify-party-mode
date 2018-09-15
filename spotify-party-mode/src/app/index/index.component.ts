import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  title = 'spotify-party-mode';
  createResponse = 'not yet clicked';
  joinResponse = 'not yet clicked';
  textBoxString = 'null';

  const httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json',
      'Authorization': 'my-auth-token'
    })
  };

  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  onCreateClick(){
    this.http.get("http://022b0446.ngrok.io/create").subscribe(response => {
      console.log(response);
      this.createResponse = response.id;
    });
  }

  onJoinClick(){
    this.http.post("http://022b0446.ngrok.io/join", this.textBoxString, this.httpOptions).subscribe(response => {
      console.log(response);
      this.joinResponse = response.title;
    });
  }

  onKey(event: any) {
    this.textBoxString = (<HTMLInputElement>event.target).value;
  }

}
