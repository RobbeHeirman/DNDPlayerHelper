type Observer<T> = (message: T) => void

class ObserverManager<T> {
    private subscribers: Observer<T>[];

    constructor() {
        this.subscribers = [];
    }

    subscribe(observer: Observer<T>) {
        this.subscribers.push(observer)
    }

    unsubscribe(observer: Observer<T>) {
        this.subscribers = this.subscribers.filter(sub => sub !== observer)
    }

    broadcast(message: T) {
        this.subscribers.forEach(func => func(message))
    }
}

export default ObserverManager