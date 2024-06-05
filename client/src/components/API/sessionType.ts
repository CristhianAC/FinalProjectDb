import axios from 'axios';

export class usuario {
    email: string;
    name: string;
    
    id: string;

    constructor(email: string, name: string, id: string) {
        this.email = email;
        this.name = name;
        
        this.id = id;
    }
}
export class SessionType {
    user: usuario;

    constructor(user: usuario) {
        this.user = user;
    }
}

