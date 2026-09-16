import torch
from torch import nn

torch.manual_seed(42)

x = torch.linspace(-1,1, 101).reshape(-1, 1)
y = x ** 2

model = nn.Sequential(
        nn.Linear(1, 8),
        nn.ReLU(),
        nn.Linear(8, 1)
)
loss_fn = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(), lr=0.01)

for _ in range(500):
    pred = model(x)
    loss = loss_fn(pred, y)
    opt.zero_grad()
    loss.backward()
    opt.step()

model.eval()
with torch.no_grad():
    final_loss =loss_fn(model(x), y)
    print(f"Final Loss: {final_loss.item():.6f}")
