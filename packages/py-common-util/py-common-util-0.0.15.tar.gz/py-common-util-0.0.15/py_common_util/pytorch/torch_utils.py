# coding: utf-8 or # -*- coding: utf-8 -*-
import torch


class TorchUtils:

    @staticmethod
    def watch_tensor(tensor):
        """
        在cpu环境下查看PyTorch的tensor
        """
        return tensor.data.cpu().numpy()

    @staticmethod
    def batchify(data, batch_size, device):
        """
        将数据按batch_size分批
        :param data:
        :param batch_size:
        :param device:
        :return:
        """
        num_batch = data.size(0) // batch_size
        # Trim off any extra elements that wouldn't cleanly fit (remainders).
        data = data.narrow(0, 0, num_batch * batch_size)
        # Evenly divide the data across the batch_size batches.
        data = data.view(batch_size, -1).t().contiguous()
        return data.to(device)

    @staticmethod
    def np_to_tensor(np_data):
        return torch.from_numpy(np_data)


if __name__ == '__main__':
    data = torch.randn(2, 5)
    print(data)
