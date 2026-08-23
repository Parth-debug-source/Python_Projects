import sys
import numpy as np
import pygame
import torch
import torch.nn as nn

# Define the Pytorch Neural Network Policy
class PolicyNet(nn.Module):
    def __init__(self):
        super(PolicyNet, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 2),
            nn.Tanh()
        )
        
    def forward(self, x):
        return self.net(x)


# Instantiate network
model = PolicyNet()

# Initialize random parameters (simulating an untrained initial model)
with torch.no_grad():
    for layer in model.net:
        if isinstance(layer, nn.Linear):
            nn.init.constant_(layer.weight, 0.5)
            nn.init.zeros_(layer.bias)  # Zero-initialize biases
# Initialize Pygame Environment
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Agent - Direct Decision Model")
clock = pygame.time.Clock()

# Agent and Target Positions [X, Y]
agent_pos = np.array([100.0, 100.0])
target_pos = np.array([700.0, 500.0])
speed = 4.0
dist_to_target = np.linalg.norm(target_pos - agent_pos)


def normalize_and_scale(vector, speed):
    """Normalizes a given vector (assumes it's not zero) and scales it by the provided speed."""
    norm = np.linalg.norm(vector)
    if norm == 0:
        return [0.0, 0.0]
    normalized_vector = vector / norm
    scaled_vector = normalized_vector * speed
    return scaled_vector


def evaluate_ai_decision(agent, target):
    """Passes state to the PyTorch neural network to predict action."""
    # State representation: relative vector to target
    relative_state = target - agent

    # Convert NumPy array to PyTorch Tensor (batch size = 1)
    state_tensor = torch.tensor(relative_state, dtype=torch.float32).unsqueeze(0)

    # Run forward pass through neural net (no gradient computation needed during inference)
    with torch.no_grad():
        action = model(state_tensor)

    # Convert tensor prediction back to NumPy array
    return action.squeeze(0).numpy()


# GAME LOOP HERE
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_dir = evaluate_ai_decision(agent_pos, target_pos)

    # Normalize and scale the movement direction to ensure proper step-by-step movement.
    agent_move_vector = normalize_and_scale(move_dir, speed)

    # Update agent position
    agent_pos += agent_move_vector

    # Rendering
    screen.fill((30, 30, 35))  # Dark background

    # Draw Target (Red) and Agent (green)
    pygame.draw.circle(screen, (200, 80, 80), target_pos.astype(int), 15)  # Target
    pygame.draw.circle(screen, (80, 220, 120), agent_pos.astype(int), 12)  # Agent

    pygame.display.flip()  # Update display
    clock.tick(30)  # Cap the frame rate to 30 FPS

pygame.quit()
sys.exit()


