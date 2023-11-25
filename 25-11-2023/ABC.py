from asyncio import run, sleep
import asyncio
import time

class SetTTL:
    def __init__(self, ttl: float = 10):
        self.s = set()
        self.value_age = {}
        self.ttl = ttl
        self.running = True

    async def periodic_message(self):
        while self.running:
            print("Komunikat co sekundę")
            await sleep(1)

    async def initialize(self):
        asyncio.create_task(self.periodic_message())  # Uruchomienie nowego tasku
        while self.running:
            current_time = time.time()
            to_remove = [item for item, added_time in self.value_age.items() if current_time - added_time > self.ttl]

            # Usuwanie przeterminowanych wartości na koniec cyklu
            for item in to_remove:
                self.remove(item)

            await sleep(0.1)

    def add(self, item):
        self.s.add(item)
        self.value_age[item] = time.time()

    def remove(self, item):
        if item in self.s:
            self.s.remove(item)
            del self.value_age[item]

    def __contains__(self, item):
        return item in self.s

    def __repr__(self):
        return self.s.__repr__()

    def stop(self):
        self.running = False

async def main():
    s = SetTTL(5)  # TTL 5 sekund
    s.add(10)
    s.add(11)
    print("Przed usunięciem:", s)
    task = asyncio.create_task(s.initialize())  # Uruchomienie asynchronicznej pętli
    await sleep(10)  # Czekanie, aby umożliwić usunięcie elementów
    s.stop()  # Zatrzymanie asynchronicznej pętli
    await task  # Upewnienie się, że pętla zakończyła działanie
    print("Po usunięciu:", s)

if __name__ == '__main__':
    run(main())
