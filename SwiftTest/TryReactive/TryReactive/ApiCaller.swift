//
//  ApiCaller.swift
//  TryReactive
//
//  Created by Motoshi Suzuki on 2021/09/11.
//

import Foundation
import Combine

class ApiCaller {
    static let shared = ApiCaller()
    
    func fetchData() -> Future<[String], Error> {
        return Future { promise in
            DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                promise(.success(["Apple", "Google", "Microsoft", "Facebook"]))
            }
        }
    }
}
