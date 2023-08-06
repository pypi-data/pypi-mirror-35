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
    def batchify(tensor_data, batch_size, device):
        """
        将数据按batch_size分批
        :param data:
        :param batch_size:
        :param device:
        :return:
        """
        num_batch = tensor_data.size(0) // batch_size
        # Trim off any extra elements that wouldn't cleanly fit (remainders).
        tensor_data = tensor_data.narrow(0, 0, num_batch * batch_size)
        # Evenly divide the data across the batch_size batches.
        tensor_data = tensor_data.view(batch_size, -1).t().contiguous()
        return tensor_data.to(device)

    @staticmethod
    def batchify_np_data_label(tuple_np_data_label, batch_size, device):
        data = TorchUtils.np_to_tensor(tuple_np_data_label[0])
        label = TorchUtils.np_to_tensor(tuple_np_data_label[1])
        batched_data = TorchUtils.batchify(data, batch_size, device)
        batched_label = TorchUtils.batchify(label, batch_size, device)
        return zip(batched_data, batched_label)

    @staticmethod
    def np_to_tensor(np_data):
        return torch.from_numpy(np_data)

    @staticmethod
    def cuda_is_available():
        return torch.cuda.is_available()


if __name__ == '__main__':
    data = torch.randn(2, 5)
    print(data)
