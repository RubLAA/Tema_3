from HanoiVisualizer import HanoiVisualizer
from HanoiCalculator import HanoiCalculator

def main(num_blocks):  # Cambia este valor para probar
    if num_blocks <= 24:
        visualizer = HanoiVisualizer(num_blocks)
        visualizer.run()
    elif num_blocks > 24:
        visualizer = HanoiCalculator(num_blocks)
        visualizer.show_result()

if __name__ == "__main__":
    main(int(input("Número de bloques: ")))