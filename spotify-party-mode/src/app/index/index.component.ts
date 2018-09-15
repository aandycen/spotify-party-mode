import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

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

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
  }

  onCreateClick(){
    this.http.get("http://1525cd2b.ngrok.io/create").subscribe(response => {
      console.log(response);
      this.createResponse = (response as any).playlistID;
      var routeDest = '/room/' + (response as any).playlistName;
      this.router.navigate([routeDest]);
      var spotifyLink = "https://open.spotify.com/playlist/" + (response as any).playlistID;
      window.open(spotifyLink);
    });
  }

  onJoinClick(){
    var postBody = {"name" : this.textBoxString};
    this.http.post("http://1525cd2b.ngrok.io/join", postBody).subscribe(response => {
      this.joinResponse = response.canJoin;
      if(response.canJoin == "True") {
        var routeDest = '/room/' + this.textBoxString;
        this.router.navigate([routeDest]);
      }
    });
  }

  onKey(event: any) {
    this.textBoxString = (<HTMLInputElement>event.target).value;
  }
}
