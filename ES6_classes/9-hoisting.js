export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this._holbertonClass;
  }

  get fullStudentDescription() {
    return `${this.fullName} - ${this.holbertonClass.year} - ${this.holbertonClass.location}`;
  }
}

export const class2019 = new HolbertonClass(2019, 'San Francisco');
export const class2020 = new HolbertonClass(2020, 'San Francisco');

export const student1 = new StudentHolberton(
  'Guillaume',
  'Salva',
  class2020,
);
export const student2 = new StudentHolberton('John', 'Doe', class2020);
export const student3 = new StudentHolberton('Albert', 'Cloning', class2019);
