from collections import deque


class Route:
    def __init__(self, start, end, transport, duration):
        self.start = start
        self.end = end
        self.transport = transport
        self.duration = duration



class TransportNetwork:
    def __init__(self, routes):
        self.routes = routes
        self.graph = self._build_graph()

    def _build_graph(self):
        """노선 데이터를 양방향 그래프로 변환"""
        graph = {}
        for r in self.routes:
            graph.setdefault(r.start, []).append((r.end, r.duration))
            graph.setdefault(r.end, []).append((r.start, r.duration))
        return graph

    def find_route(self, start, end):
        """BFS로 출발~도착 경로 및 총 이동시간 탐색"""
        queue = deque([(start, [start], 0)])  # (현재역, 경로, 누적시간)
        visited = set([start])

        while queue:
            station, path, total = queue.popleft()
            if station == end:
                return path, total

            for neighbor, duration in self.graph.get(station, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor], total + duration))
        return None, None



class TransportSystem:
    def __init__(self):
        self.network = None
        self.transport_type = None

    def read_txt(self, filename):
        """txt 파일에서 노선 데이터 읽기"""
        routes = []
        try:
            with open(filename, mode='r', encoding='utf-8-sig') as file:
                next(file)  # 헤더 건너뛰기
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        try:
                            routes.append(Route(
                                start=parts[0],
                                end=parts[1],
                                transport=parts[2],
                                duration=int(parts[3])
                            ))
                        except ValueError:
                            print(f"⚠ 이동시간 변환 오류: {line.strip()}")
                    else:
                        print(f"⚠ 잘못된 데이터 형식: {line.strip()}")
        except FileNotFoundError:
            print(f"❌ 파일 '{filename}'을(를) 찾을 수 없습니다.")
        return routes

    def choose_transport(self):
        """사용자에게 교통수단 선택 입력 받기"""
        print("\n=== 교통수단 선택 ===")
        while True:
            t = input("지하철 또는 버스를 입력하세요: ").strip()
            if t in ("지하철", "버스"):
                self.transport_type = t
                break
            print("⚠ 잘못된 입력입니다. 다시 입력하세요.")

    def load_data(self):
        """선택된 교통수단에 맞는 데이터 불러오기"""
        filename = 'station.txt' if self.transport_type == "지하철" else 'bus station.txt'
        routes = self.read_txt(filename)
        self.network = TransportNetwork(routes)

    def run(self):
        """프로그램 실행"""
        self.choose_transport()
        self.load_data()

        start = input("출발역(정류장)을 입력하세요: ").strip()
        end = input("도착역(정류장)을 입력하세요: ").strip()

        path, total_time = self.network.find_route(start, end)

        if path:
            print(f"\n=== {self.transport_type} 경로 결과 ===")
            print(" → ".join(path))
            print(f"총 {len(path)-1}개 구간 이동")
            print(f"총 소요 시간: {total_time}분")
            print("===========================")
        else:
            print(f"⚠ '{start}'에서 '{end}'로 가는 {self.transport_type} 경로를 찾을 수 없습니다.")



if __name__ == "__main__":
    system = TransportSystem()
    system.run()

   