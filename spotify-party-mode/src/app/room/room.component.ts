import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-room',
  templateUrl: './room.component.html',
  styleUrls: ['./room.component.css']
})
export class RoomComponent implements OnInit {
  id: string;
  private sub: any;
  textBoxString = '';

  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
           this.id = params['id'];
        });
  }

  onAddClick(){
    this.http.get("http://1525cd2b.ngrok.io/add").subscribe(response => {
      console.log(response);
      this.joinResponse = response.title;
    });
  }

  onKey(event: any) {
    this.textBoxString = (<HTMLInputElement>event.target).value;
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }
}
