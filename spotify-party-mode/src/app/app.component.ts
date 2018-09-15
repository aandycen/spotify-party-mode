import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'spotify-party-mode';
  createResponse = 'not yet clicked';

  constructor(private http: HttpClient) { }

  onCreateClick(){
    this.http.get("http://localhost:5000/hello").subscribe(response => {
      console.log(response);
      this.createResponse = response.id;
    });
  }
}
