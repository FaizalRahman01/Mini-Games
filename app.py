import tkinter as tk
import random

# Game constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SPEED = 150  # milliseconds

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)
        
        # Canvas create karo
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        # Score display
        self.score_label = tk.Label(self.window, text="Score: 0", font=('Arial', 14))
        self.score_label.pack()
        
        # Game variables
        self.snake = [(100, 100), (80, 100), (60, 100)]  # [head, body, tail]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        
        # Controls bind karo
        self.window.bind('<KeyPress>', self.change_direction)
        self.canvas.focus_set()
        
        # Game start karo
        self.update()
        
        self.window.mainloop()
    
    def create_food(self):
        """Random position par food create karo"""
        while True:
            x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            food_pos = (x, y)
            
            # Ensure food snake ke upar nahi hai
            if food_pos not in self.snake:
                return food_pos
    
    def change_direction(self, event):
        """Keyboard input handle karo"""
        key = event.keysym
        
        # Opposite direction me nahi ja sakta
        if (key == "Up" and self.direction != "Down" or
            key == "Down" and self.direction != "Up" or
            key == "Left" and self.direction != "Right" or
            key == "Right" and self.direction != "Left"):
            self.direction = key
    
    def move_snake(self):
        """Snake ko move karo"""
        if self.game_over:
            return
        
        # Naya head position calculate karo
        head_x, head_y = self.snake[0]
        
        if self.direction == "Up":
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + GRID_SIZE, head_y)
        
        # Game over conditions check karo
        if (new_head in self.snake or 
            new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return
        
        # Naya head add karo
        self.snake.insert(0, new_head)
        
        # Food check karo
        if new_head == self.food:
            # Score badhao aur naya food banao
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.create_food()
        else:
            # Tail remove karo agar food nahi khaya
            self.snake.pop()
    
    def draw(self):
        """Screen draw karo"""
        self.canvas.delete("all")
        
        # Food draw karo
        self.canvas.create_rectangle(
            self.food[0], self.food[1],
            self.food[0] + GRID_SIZE, self.food[1] + GRID_SIZE,
            fill="red", outline=""
        )
        
        # Snake draw karo
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1],
                segment[0] + GRID_SIZE, segment[1] + GRID_SIZE,
                fill="green", outline=""
            )
        
        # Game over message
        if self.game_over:
            self.canvas.create_text(
                WIDTH // 2, HEIGHT // 2,
                text=f"Game Over! Score: {self.score}\nPress R to restart",
                fill="white", font=('Arial', 20),
                justify=tk.CENTER
            )
    
    def update(self):
        """Game update karo"""
        if not self.game_over:
            self.move_snake()
            self.draw()
            self.window.after(SPEED, self.update)  # Next update schedule karo
        else:
            # Restart functionality
            self.window.bind('r', self.restart_game)
            self.window.bind('R', self.restart_game)
    
    def restart_game(self, event=None):
        """Game restart karo"""
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        self.score_label.config(text="Score: 0")
        self.window.unbind('r')
        self.window.unbind('R')
        self.update()

# Game start karo
if __name__ == "__main__":
    SnakeGame()