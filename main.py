import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
DATA_FILE = "tasks.json"

class NextGenToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Next-Gen To-Do App")
        self.root.geometry("550x600")
        self.tasks = []
        self.load_tasks()

        self.title_label = ctk.CTkLabel(root, text="✅ Task Manager", font=("Segoe UI", 24, "bold"))
        self.title_label.pack(pady=15)

        self.task_entry = ctk.CTkEntry(root, placeholder_text="Enter your task...", width=400)
        self.task_entry.pack(pady=10)

        self.add_btn = ctk.CTkButton(root, text="➕ Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.task_frame = ctk.CTkFrame(root, height=400)
        self.task_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.refresh_tasks()

        self.toggle_btn = ctk.CTkButton(root, text="🌗 Toggle Theme", command=self.toggle_theme)
        self.toggle_btn.pack(pady=10)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            self.task_entry.delete(0, 'end')
            self.save_tasks()
            self.refresh_tasks()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def toggle_done(self, idx):
        self.tasks[idx]["done"] = not self.tasks[idx]["done"]
        self.save_tasks()
        self.refresh_tasks()

    def delete_task(self, idx):
        del self.tasks[idx]
        self.save_tasks()
        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks):
            color = "green" if task["done"] else "gray"
            text = f"{'✅' if task['done'] else '❌'} {task['task']}"

            task_row = ctk.CTkFrame(self.task_frame)
            task_row.pack(fill="x", pady=5, padx=10)

            task_label = ctk.CTkLabel(task_row, text=text, text_color=color, anchor="w", width=340)
            task_label.pack(side="left", padx=5)

            done_btn = ctk.CTkButton(task_row, text="✔️", width=40, command=lambda idx=index: self.toggle_done(idx))
            done_btn.pack(side="left", padx=5)

            del_btn = ctk.CTkButton(task_row, text="🗑️", width=40, fg_color="red", command=lambda idx=index: self.delete_task(idx))
            del_btn.pack(side="right", padx=5)

    def save_tasks(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.tasks = json.load(f)

    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        new_mode = "Light" if current == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)


if __name__ == "__main__":
    root = ctk.CTk()
    app = NextGenToDo(root)
    root.mainloop()
