//
//  ViewController.swift
//  TryReactive
//
//  Created by Motoshi Suzuki on 2021/09/11.
//

import UIKit
import Combine

class ViewController: UIViewController, UITableViewDataSource {
    
    private let tableView: UITableView = {
        let table = UITableView()
        table.register(CustomTableCell.self, forCellReuseIdentifier: "cell")
        return table
    }()
    
    var observers: [AnyCancellable] = []
    private var models = [String]()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        view.addSubview(tableView)
        tableView.dataSource = self
        tableView.frame = view.bounds
        
        ApiCaller.shared.fetchData()
            .receive(on: DispatchQueue.main)
            .sink(receiveCompletion: { completion in
                switch completion {
                case .finished:
                    print("Finished")
                case .failure(let error):
                    print(error.localizedDescription)
                }
            }, receiveValue: { [weak self] value in
                self?.models = value
                self?.tableView.reloadData()
            }).store(in: &observers)
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return models.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as? CustomTableCell else {
            fatalError()
        }
        cell.action.sink { string in
            print(string)
        }.store(in: &observers)
        
        return cell
    }
}

class CustomTableCell: UITableViewCell {
    
    private let button: UIButton = {
        let button = UIButton()
        button.backgroundColor = .systemPink
        button.setTitle("Button", for: .normal)
        button.setTitleColor(.white, for: .normal)
        return button
    }()
    
    let action = PassthroughSubject<String, Never>()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        contentView.addSubview(self.button)
        self.button.addTarget(self, action: #selector(didTapButton), for: .touchUpInside)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    @objc private func didTapButton() {
        action.send("Cool, button was tapped!!")
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        self.button.frame = CGRect(x: 10, y: 3, width: contentView.frame.size.width - 20, height: contentView.frame.size.height - 6)
    }
}

