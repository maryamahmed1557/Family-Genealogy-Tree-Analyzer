from AI_Project import *
import customtkinter as ctk
import tkinter as tk

# ================= APP =================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Family Tree Analyzer")
app.geometry("1200x700")

# ================= STATE =================
highlight_nodes = set()
positions = {}
current_node = None

scale = 1.0
offset_x = 0
offset_y = 0
drag_start = None

# ================= LAYOUT =================
sidebar = ctk.CTkFrame(app, width=300)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

main_area = ctk.CTkFrame(app)
main_area.pack(side="right", fill="both", expand=True)

canvas = tk.Canvas(main_area, bg="#0f172a", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ================= INPUT =================
name_entry = ctk.CTkEntry(sidebar, placeholder_text="Enter Name")
name_entry.pack(pady=10, padx=10, fill="x")

name_entry2 = ctk.CTkEntry(sidebar, placeholder_text="Second Name (LCA)")
name_entry2.pack(pady=10, padx=10, fill="x")

output_box = ctk.CTkTextbox(sidebar, height=100)
output_box.pack(pady=10, padx=10, fill="x")

# ================= INFO PANEL =================
info_frame = ctk.CTkFrame(sidebar)
info_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(info_frame, text="Node Info", font=("Arial", 14, "bold")).pack()

info_text = ctk.CTkTextbox(info_frame, height=140)
info_text.pack(pady=5, padx=5, fill="x")

# ================= ERROR =================
def show_error(msg):
    output_box.delete("0.0", "end")
    output_box.insert("0.0", f"❌ {msg}")

# ================= BUTTON =================
def btn(text, cmd):
    return ctk.CTkButton(sidebar, text=text, command=cmd, corner_radius=12, height=35)

# ================= TRANSFORM =================
def transform(x, y):
    return x * scale + offset_x, y * scale + offset_y

# ================= TREE LAYOUT =================
def build_levels(root):
    levels = {}

    def dfs(p, d):
        if not p:
            return
        levels.setdefault(d, []).append(p)
        for c in p.children:
            dfs(c, d + 1)

    dfs(root, 0)
    return levels


def generate_positions():
    global positions
    positions = {}

    levels = build_levels(adam)

    x_gap = 150
    y_gap = 120

    for d, nodes in levels.items():
        start_x = 600 - (len(nodes) * x_gap) // 2

        for i, node in enumerate(nodes):
            positions[node.name] = (start_x + i * x_gap, 80 + d * y_gap)

# ================= DRAW =================
def draw_tree():
    canvas.delete("all")

    # edges
    for p in family_dict.values():
        if p.name in positions:
            x1, y1 = transform(*positions[p.name])

            for parent in [p.father, p.mother]:
                if parent and parent.name in positions:
                    x2, y2 = transform(*positions[parent.name])

                    color = "#facc15" if (p.name in highlight_nodes and parent.name in highlight_nodes) else "#334155"

                    canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

    # nodes
    for name, (x, y) in positions.items():
        x, y = transform(x, y)

        if name == current_node:
            color = "#facc15"
        elif name in highlight_nodes:
            color = "#34d371"
        else:
            color = "#38bdf8"

        if name == current_node:
            canvas.create_oval(x-28, y-28, x+28, y+28, outline="#facc15", width=3)

        canvas.create_oval(x-22, y-22, x+22, y+22, fill=color, outline="")
        canvas.create_text(x, y, text=name, fill="white", font=("Segoe UI", 10, "bold"))

# ================= INFO =================
def show_node_info(name):
    p = family_dict[name]

    info_text.delete("0.0", "end")
    info_text.insert(
        "0.0",
        f"Name: {name}\n"
        f"Father: {p.father.name if p.father else 'None'}\n"
        f"Mother: {p.mother.name if p.mother else 'None'}\n"
        f"Children: {[c.name for c in p.children]}\n"
        f"Depth: {get_generation_depth(p)}"
    )

# ================= SIBLINGS =================
def get_siblings(person):
    siblings = set()
    parents = [p for p in [person.father, person.mother] if p]

    for parent in parents:
        for child in parent.children:
            if child != person:
                siblings.add(child.name)

    return list(siblings)

# ================= PATH TO ANCESTOR =================
def get_path_to_ancestor(person, ancestor_name):
    path = []
    visited = set()

    def dfs(p):
        if not p or p in visited:
            return False

        visited.add(p)
        path.append(p.name)

        if p.name == ancestor_name:
            return True

        for parent in [p.father, p.mother]:
            if dfs(parent):
                return True

        path.pop()
        return False

    dfs(person)
    return path

# ================= ACTIONS =================
def show_ancestors():
    name = name_entry.get().capitalize()

    if name not in family_dict:
        show_error("Invalid name")
        return

    p = family_dict[name]
    result = get_ancestors(p)

    highlight_nodes.clear()
    highlight_nodes.add(name)
    highlight_nodes.update(result)

    output_box.delete("0.0", "end")
    output_box.insert("0.0", "Ancestors:\n" + "\n".join(result))

    draw_tree()


def show_descendants():
    name = name_entry.get().capitalize()

    if name not in family_dict:
        show_error("Invalid name")
        return

    p = family_dict[name]
    result = get_descendants(p)

    highlight_nodes.clear()
    highlight_nodes.add(name)
    highlight_nodes.update(result)

    output_box.delete("0.0", "end")
    output_box.insert("0.0", "Descendants:\n" + "\n".join(result))

    draw_tree()


def show_siblings():
    name = name_entry.get().capitalize()

    if name not in family_dict:
        show_error("Invalid name")
        return

    p = family_dict[name]
    result = get_siblings(p)

    highlight_nodes.clear()
    highlight_nodes.add(name)
    highlight_nodes.update(result)

    output_box.delete("0.0", "end")
    output_box.insert("0.0", "Siblings:\n" + "\n".join(result))

    draw_tree()


def show_depth():
    name = name_entry.get().capitalize()

    if name not in family_dict:
        show_error("Invalid name")
        return

    p = family_dict[name]
    result = get_generation_depth(p)

    output_box.delete("0.0", "end")
    output_box.insert("0.0", f"Generation Depth: {result}")


def run_lca():
    n1 = name_entry.get().capitalize()
    n2 = name_entry2.get().capitalize()

    if n1 not in family_dict or n2 not in family_dict:
        show_error("Invalid name(s)")
        return

    p1 = family_dict[n1]
    p2 = family_dict[n2]

    lca_name = get_lca(p1, p2)

    if lca_name == "No Common Ancestor":
        output_box.delete("0.0", "end")
        output_box.insert("0.0", "No Common Ancestor")
        return

    highlight_nodes.clear()

    path1 = get_path_to_ancestor(p1, lca_name)
    path2 = get_path_to_ancestor(p2, lca_name)

    highlight_nodes.update(path1)
    highlight_nodes.update(path2)
    highlight_nodes.add(lca_name)

    output_box.delete("0.0", "end")
    output_box.insert("0.0", f"LCA: {lca_name}")

    draw_tree()


def search():
    name = name_entry.get().capitalize()

    if name not in family_dict:
        show_error("Invalid name")
        return

    highlight_nodes.clear()
    highlight_nodes.add(name)
    draw_tree()
    show_node_info(name)

# ================= ZOOM =================
def zoom(event):
    global scale
    scale *= 1.1 if event.delta > 0 else 0.9
    draw_tree()

# ================= PAN =================
def start_drag(event):
    global drag_start
    drag_start = (event.x, event.y)


def do_drag(event):
    global offset_x, offset_y, drag_start

    dx = event.x - drag_start[0]
    dy = event.y - drag_start[1]

    offset_x += dx
    offset_y += dy

    drag_start = (event.x, event.y)

    draw_tree()


def stop_drag(event):
    global drag_start
    drag_start = None

canvas.bind("<MouseWheel>", zoom)
canvas.bind("<ButtonPress-1>", start_drag)
canvas.bind("<B1-Motion>", do_drag)
canvas.bind("<ButtonRelease-1>", stop_drag)

# ================= BUTTONS =================
btn("🌿 Ancestors", show_ancestors).pack(pady=5, padx=10, fill="x")
btn("🌱 Descendants", show_descendants).pack(pady=5, padx=10, fill="x")
btn("👥 Siblings", show_siblings).pack(pady=5, padx=10, fill="x")
btn("📊 Generation Depth", show_depth).pack(pady=5, padx=10, fill="x")
btn("🧬 LCA", run_lca).pack(pady=5, padx=10, fill="x")
btn("🔍 Search", search).pack(pady=5, padx=10, fill="x")

# ================= START =================
generate_positions()
draw_tree()

app.mainloop()