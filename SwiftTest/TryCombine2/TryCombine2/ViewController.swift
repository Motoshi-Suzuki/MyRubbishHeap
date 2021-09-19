//
//  ViewController.swift
//  TryCombine2
//
//  Created by Motoshi Suzuki on 2021/09/17.
//

import UIKit
import Combine

class UsersTableViewController: UITableViewController {
    
    private var usersSubscriber: AnyCancellable?
    
    private var users = [User]() {
        didSet {
            tableView.reloadData()
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        setUpTableView()
        fetchUsers()
    }
    
    private func fetchUsers() {
        usersSubscriber = DataManager().usersPublisher
            .sink(receiveCompletion: { _ in
                print("Received Data !!")
            }, receiveValue: { (users) in
                self.users = users
            })
    }
    
    private func setUpTableView() {
        tableView.tableFooterView = UIView()
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.users.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .subtitle, reuseIdentifier: nil)
        let user = self.users[indexPath.item]
        cell.textLabel?.text = user.name
        cell.detailTextLabel?.text = user.company.name
        return cell
    }

}

