import os

def write_directory_structure():
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(base_path, 'structure.txt'), 'w', encoding='utf-8') as f:
        current_dir_name = os.path.basename(base_path) or os.path.basename(os.path.dirname(base_path)) + '/'
        f.write(f"{current_dir_name}/\n")
        
        for root, dirs, files in os.walk(base_path):
            level = root.replace(base_path, '').count(os.sep)
            indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
            
            if root != base_path:
                dir_name = os.path.basename(root)
                f.write(f"{indent}{dir_name}/\n")
            
            sub_indent = '│   ' * level + '├── '
            for file in sorted(files):
                f.write(f"{sub_indent}{file}\n")

if __name__ == "__main__":
    write_directory_structure()