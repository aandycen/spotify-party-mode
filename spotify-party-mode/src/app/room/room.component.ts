import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-room',
  templateUrl: './room.component.html',
  styleUrls: ['./room.component.css']
})
export class RoomComponent implements OnInit {
  id: string;
  textBoxString = '';

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {

  }

  onAddClick(){
    this.http.get("http://022b0446.ngrok.io/add").subscribe(response => {
      console.log(response);
      this.joinResponse = response.title;
    });
  }

  onKey(event: any) {
    this.textBoxString = (<HTMLInputElement>event.target).value;
  }

}
