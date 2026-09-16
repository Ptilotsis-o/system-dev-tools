import torch
from torch import nn

torch.manual_seed(42)

x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 2 * x + 5

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.05)

for _ in range(300):
    pred = model(x)
    loss = loss_fn(pred, y)
    opt.zero_grad()
    loss.backward()
    opt.step()

model.eval()
with torch.no_grad():
    final_loss = loss_fn(model(x), y)
    print(f"Final Loss: {final_loss.item():.6f}")
    print(f"Weight: {model.weight.item():.4f}, Bias: {model.bias.item():.4f}")
