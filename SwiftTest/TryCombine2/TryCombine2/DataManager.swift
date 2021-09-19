//
//  DataManager.swift
//  TryCombine2
//
//  Created by Motoshi Suzuki on 2021/09/18.
//

import Foundation
import Combine

class DataManager {
    
    private let urlString = "https://jsonplaceholder.typicode.com/users"
    
    var usersPublisher: AnyPublisher<[User], Error> {
        let url = URL(string: urlString)!
        print("Data will be published")
        
        return URLSession.shared.dataTaskPublisher(for: url)
            .map { $0.data }
            .decode(type: [User].self, decoder: JSONDecoder())
            .receive(on: RunLoop.main)
            .eraseToAnyPublisher()
        
    }
}
