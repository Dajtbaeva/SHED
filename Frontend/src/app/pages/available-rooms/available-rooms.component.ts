import { Component, OnInit } from '@angular/core';
import { IRoom } from 'src/app/models/room';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-available-rooms',
  templateUrl: './available-rooms.component.html',
  styleUrls: ['./available-rooms.component.css'],
})
export class AvailableRoomsComponent implements OnInit {
  hour = 0;
  day = '';
  rooms: IRoom[] = [];
  invalid = false;
  is_loading = false;
  days = [
    { name: 'Monday' },
    { name: 'Tuesday' },
    { name: 'Wednesday' },
    { name: 'Thursday' },
    { name: 'Friday' },
    { name: 'Saturday' },
  ];

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.getCurrentAvailableRooms();
  }
  getCurrentAvailableRooms() {
    const currentDate = new Date();
    this.hour = currentDate.getHours();
    const day = currentDate.getDay().toString();
    this.day = this.days[currentDate.getDay() - 1].name; // return number
    this.is_loading = true;
    if (this.hour > 7 && this.hour < 21 && day !== '') {
      this.userService
        .getAvailableRooms(this.hour, day)
        .subscribe((data) => (this.rooms = data));
      this.is_loading = false;
    } else {
      this.invalid = true;
      this.is_loading = false;
    }
  }
  updateAvailableRooms() {
    this.is_loading = true;
    const day = this.days
      .findIndex((d) => d.name === this.day.trim())
      .toString();
    this.userService.getAvailableRooms(this.hour, day).subscribe((data) => {
      this.rooms = data;
      this.is_loading = false;
      this.invalid = false;
    });
  }
  onChange() {
    this.updateAvailableRooms();
  }
}
