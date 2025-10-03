import rclpy
from rclpy.executors import MultiThreadedExecutor

from topic_service_action_rclpy_example.calculator.calculator import Calculator

def main(args = None):
    rclpy.init(args=args)
    try:
        calcuator = Calculator()
        executor = MultiThreadedExecutor(num_threads=4)
        executor.add_node(calcuator)
        try:
            executor.spin()
        except KeyboardInterrupt:
            calcuator.get_logger().info('Keyboard Interrupt (SIGINT)')
        finally:
            executor.shutdown()
            calcuator.arithmetic_action_server.destroy()
            calcuator.destory_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()