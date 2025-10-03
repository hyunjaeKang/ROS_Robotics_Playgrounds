import random

from msg_srv_action_interface_example.srv import ArithmeticOperator
import rclpy
from rclpy.node import Node

class Operator(Node):
    def __init__(self):
        super().__init__('operator')

        self.arithmetic_service_client = self.create_client(
            ArithmeticOperator,
            'arithmetic_operator'
        )

        while not self.arithmetic_service_client.wait_for_service(timeout_sec=0.1):
            self.get_logger().warning('The arithmetic operator service not available')

    def send_request(self):
        service_request = ArithmeticOperator.Request()
        service_request.arithmetic_operator = random.randint(1, 4)
        futures = self.arithmetic_service_client.call_async(service_request)
        return futures
    
def main(args = None):
    rclpy.init(args=args)
    operator = Operator()
    future = operator.send_request()
    user_trigger = True
    try:
        while rclpy.ok():
            if user_trigger is True:
                rclpy.spin_once(operator)
                if future.done():
                    try:
                        service_request = future.result()
                    except Exception as e:
                        operator.get_logger().warn(f'Service call failed {str(e)}')
                    else:
                        operator.get_logger().info(
                            f'Result {service_request.arithmetic_result}')
                        user_trigger = False
            else:
                input('Press Ender for next service call')
                future = operator.send_request()
                user_trigger = True
    except KeyboardInterrupt:
        operator.get_logger().info('Keyboard Interrupt (SIGINT)')
    
    operator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
