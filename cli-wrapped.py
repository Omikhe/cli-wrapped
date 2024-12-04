import os
from collections import Counter
import datetime

class CLIWrapped:
    def __init__(self, history_file=None):
        # Default to standard .bash_history location if not specified
        self.history_file = history_file or os.path.expanduser('~/.bash_history')
        self.commands = self.load_history()

    def load_history(self):
        """Load commands from bash history file"""
        try:
            with open(self.history_file, 'r') as f:
                # Read lines, strip whitespace, remove empty lines
                return [cmd.strip() for cmd in f.readlines() if cmd.strip()]
        except FileNotFoundError:
            print(f"Error: History file {self.history_file} not found!")
            return []

    def get_top_commands(self, n=10):
        """Analyze most frequently used commands"""
        # Split full commands and count base commands
        base_commands = [cmd.split()[0] for cmd in self.commands]
        return Counter(base_commands).most_common(n)

    def get_command_categories(self):
        """Categorize commands"""
        categories = {
            'System': ['sudo', 'apt', 'yum', 'brew', 'systemctl'],
            'Navigation': ['cd', 'pwd', 'ls', 'mkdir', 'rmdir'],
            'File Management': ['cp', 'mv', 'rm', 'touch', 'chmod'],
            'Network': ['ping', 'ssh', 'curl', 'wget', 'netstat'],
            'Development': ['git', 'npm', 'python', 'pip', 'docker']
        }
        
        category_counts = {cat: 0 for cat in categories}
        
        for cmd in self.commands:
            base_cmd = cmd.split()[0]
            for cat, cmds in categories.items():
                if base_cmd in cmds:
                    category_counts[cat] += 1
        
        return sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

    def get_daily_command_frequency(self):
        """Analyze command frequency by time"""
        # This would require timestamps in history file
        # Simplified example
        total_commands = len(self.commands)
        avg_daily_commands = total_commands / 365
        return avg_daily_commands

    def generate_cli_wrapped(self):
        """Generate a fun CLI Wrapped report"""
        print("🖥️  YOUR CLI WRAPPED 🖥️")
        print("=" * 30)
        
        # Total Commands
        print(f"\n📊 Total Commands Executed: {len(self.commands)}")
        
        # Top Commands
        print("\n🏆 Top 10 Most Used Commands:")
        for cmd, count in self.get_top_commands():
            print(f"- {cmd}: {count} times")
        
        # Command Categories
        print("\n🧑‍💻 Command Category Breakdown:")
        for cat, count in self.get_command_categories():
            print(f"- {cat}: {count} commands")
        
        # Daily Command Average
        print(f"\n⏰ Average Daily Commands: {self.get_daily_command_frequency():.2f}")
        
        # Fun Personality Based on Commands
        print("\n🎉 Your CLI Personality:")
        self._assign_cli_personality()

    def _assign_cli_personality(self):
        """Assign a fun CLI personality based on command usage"""
        top_commands = dict(self.get_top_commands())
        
        personalities = {
            'The Sysadmin': 'sudo' in top_commands,
            'The Developer': 'git' in top_commands,
            'The Network Ninja': 'ssh' in top_commands,
            'The File Wizard': 'mv' in top_commands or 'cp' in top_commands,
            'The Explorer': 'cd' in top_commands
        }
        
        for personality, condition in personalities.items():
            if condition:
                print(f"You are: {personality} 🚀")
                return
        
        print("Mysterious CLI Maestro 🕵️")

def main():
    wrapped = CLIWrapped()
    wrapped.generate_cli_wrapped()

if __name__ == "__main__":
    main()
